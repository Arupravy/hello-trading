# Hello Trading

A simple trading simulation project to demonstrate basic trading strategies. This project includes a Dockerized environment and a CI/CD pipeline for automated testing and deployment.

## Features

- **Trading Simulation**: Simulates basic trading strategies.
- **Docker Support**: Containerized environment for easy deployment.
- **CI/CD Pipeline**: Automated testing and Docker image builds using GitHub Actions.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Docker (optional, for containerized deployment)
- Git (for version control)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Arupravy/hello-trading.git
   cd hello-trading

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. (Optional) Install the project in editable mode:
    ```bash
   pip install -e .

### Running the Simulation

- To run the simulation locally:
   ```bash
   python src/main.py

### Running Tests

- To run the tests:
   ```bash
   pytest tests/

### Docker Support

- Build the Docker Image:
   ```bash
   docker build -t hello-trading .

- Run the Docker Container
   ```bash
   docker run hello-trading

### Push the Docker Image to Docker Hub

1. Log in to Docker Hub:
   ```bash
   docker login -u <your-dockerhub-username>
   
2. Tag the image:
   ```bash
   docker tag hello-trading <your-dockerhub-username>/hello-trading:latest

3. Push the image:
    ```bash
   docker push <your-dockerhub-username>/hello-trading:latest

## CI/CD Pipeline

This project includes a GitHub Actions workflow for automated testing and Docker image builds. The workflow:

- Runs tests on every push to the `main` branch.
- Builds and pushes a Docker image to Docker Hub on successful tests.

To view the workflow, check the [.github/workflows/ci-cd.yml](.github/workflows/ci-cd.yml) file.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the open-source community for providing tools and libraries that made this project possible.


    
---
## **Key Updates**
1. **Features Section**: Added Docker and CI/CD pipeline details.
2. **Installation**: Added instructions for Docker and CI/CD.
3. **Running the Simulation**: Added commands for running the simulation and tests.
4. **Docker Support**: Added detailed instructions for building, running, and pushing Docker images.
5. **CI/CD Pipeline**: Added a section explaining the GitHub Actions workflow.
6. **Contributing**: Added guidelines for contributing to the project.

---