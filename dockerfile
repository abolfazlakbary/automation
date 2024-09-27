# Base installation
FROM python:3.12
ENV DEBIAN_FRONTEND=noninteractive

# Update packages
RUN apt update

# Download Go v1.21
RUN wget https://go.dev/dl/go1.21.0.linux-amd64.tar.gz && \
    tar -C /usr/local -xzf go1.21.0.linux-amd64.tar.gz && \
    rm go1.21.0.linux-amd64.tar.gz

# Set environment variables
ENV GOROOT=/usr/local/go
ENV GOPATH=/go
ENV PATH=$GOPATH/bin:$GOROOT/bin:$PATH

# Install Nuclei and update its templates
RUN go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
RUN nuclei -ut

# Install SubEnum and its dependencies
RUN git clone https://github.com/bing0o/SubEnum.git && \
    cd SubEnum && \
    chmod +x setup.sh && \
    ./setup.sh

# Initilization of project codes
WORKDIR /app
COPY automation/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY automation/ .
COPY core/config/configs.json.sample core/config/configs.json
RUN mkdir -p files && \
    mkdir -p files/subenum && \
    mkdir -p files/nuclei

# Expose desired port
EXPOSE 1256

# Run the program
CMD ["python3", "main.py"]