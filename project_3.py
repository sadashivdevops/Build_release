# Function to build and release a microservice
import subprocess

# Function to increment the version number based on the provided rules
def increment_version(version):
    major, minor, patch = map(int, version.split('.'))
    if patch < 9:
        patch += 1
    else:
        patch = 0
        if minor < 9:
            minor += 1
        else:
            minor = 0
            major += 1
    return f"{major}.{minor}.{patch}"
def build_and_release_microservice():
    service_name = input("Enter the microservice name: ")
    current_version = input("Enter the current version (e.g., 1.0.0): ")

    # Increment version number
    new_version = increment_version(current_version)

    # Simulate build process (replace with actual build commands)
    print(f"Building {service_name} with version {new_version}")

    # Simulate tagging release in the microservice's repository

    print(f"Tagging release for {service_name} with version {new_version}")

    # Simulate releasing the microservice with the new version
    print(f"Microservice {service_name} has been released with version {new_version}")


# Main function to build and release all microservices
def build_and_release_all_microservices():
    # List of microservices and their current versions (in a real scenario, this data would come from a configuration or database)
    microservices_data = {
        "MicroserviceA": "1.0.0",
        "MicroserviceB": "1.2.3",
        # Add other microservices as needed
    }

    # Simulating user input for each microservice
    for service, version in microservices_data.items():
        build_and_release_microservice()


# Simulating deployment of all microservices with the latest versions
def deploy_all_microservices():
    print("Simulating deployment of all microservices with the latest versions")


# Example usage
build_and_release_all_microservices()
deploy_all_microservices()
