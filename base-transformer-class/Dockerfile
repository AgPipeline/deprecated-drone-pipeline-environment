FROM agpipeline/base-image:1.0
LABEL maintainer="Chris Schnaufer <schnaufer@email.arizona.edu>"

# We need to explicitly set the user to root to install in system folders
USER root

# Install Python updates
RUN python3 -m pip install --upgrade --no-cache-dir pip
RUN python3 -m pip install --upgrade --no-cache-dir setuptools

# Install applications we need
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3-gdal \
        gdal-bin   \
        libgdal-dev  \
        gcc \
        g++ \
        python3-dev && \
    python3 -m pip install --upgrade --no-cache-dir \
        pygdal==2.2.3.5 && \
    apt-get remove -y \
        libgdal-dev \
        gcc \
        g++ \
        python3-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN python3 -m pip install --upgrade --no-cache-dir \
        numpy \
        influxdb \
        laspy \
        requests==2.21.0 \
        python-dateutil \
        utm \
        matplotlib \
        Pillow \
        scipy \
        piexif

# Set to the user we want to be
USER extractor

COPY *.py /home/extractor/