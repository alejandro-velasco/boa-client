ARG BASE_REGISTRY=registry.access.redhat.com
ARG BASE_IMAGE=ubi9-minimal
ARG BASE_TAG=9.2-691

#### Start first stage
#### boa client wheels, binary dependencies, etc.
FROM ${BASE_REGISTRY}/${BASE_IMAGE}:${BASE_TAG} as boa-client-builder

# Copy build files
COPY . /src

# Set working directory to src directory
WORKDIR /src

# installing build dependencies
RUN set -ex &&                               \
    echo "installing build dependencies" &&  \
    # keepcache is used so that subsequent invocations of yum do not remove the cached RPMs in --downloaddir
    echo "keepcache = 1" >> /etc/yum.conf && \
    microdnf update -y &&                    \
    microdnf install -y                      \
        python3.11-devel                     \
        python3.11-pip                       \
        python3.11-pytest

# installing pip dependencies
RUN set -ex &&                \
    python3.11 -m pip install \
        build                 \
        pytest

# Build pip package
RUN set -ex && \
    python3.11 -m build

# Run pytest unit tests
RUN set -ex &&                                 \
    python3.11 -m pip install                  \
        dist/boa_client-0.0.1-py3-none-any.whl

RUN set -ex && \
    python3.11 -m pytest

#### Start second stage
#### final boa-client image
FROM ${BASE_REGISTRY}/${BASE_IMAGE}:${BASE_TAG}

# Copy artifacts from first stage
COPY --from=boa-client-builder /src/dist /dist
COPY entrypoint.sh /entrypoint.sh

# Install python packages and pip dependencies
RUN set -ex &&                \
    microdnf install -y       \
        shadow-utils          \
        git                   \
        python3.11            \
        python3.11-pip &&     \
    python3.11 -m pip install \
        virtualenv

# Create boa-client user and set permissions
RUN set -ex                                                                        && \
    groupadd --gid 1000 boa-client                                                 && \
    useradd --uid 1000 --gid boa-client --shell /bin/bash --create-home boa-client && \
    chown 1000:1000 -R                                                                \
        /entrypoint.sh                                                             && \
    chmod 500                                                                         \
        /entrypoint.sh

# Install boa-client into python virtual environment 
RUN set -ex                                    && \
    python3.11 -m virtualenv /boa-client       && \
    source /boa-client/bin/activate            && \
    python3.11 -m pip install                     \
        dist/boa_client-0.0.1-py3-none-any.whl && \
    rm -rf /dist                               && \
    deactivate

USER 1000

WORKDIR /home/boa-client

ENTRYPOINT ["/entrypoint.sh"]