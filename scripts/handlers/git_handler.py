import subprocess, os

def run_command(command: list):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {"output": result.stdout.strip()}
    except subprocess.CalledProcessError as e:
        return {"error": e.stderr.strip()}

# Clone the GitHub repository to the home directory
def clone_github_repo(github_url: str, repo_name: str, destination_dir: str = "/home/ubuntu"):
    try:
        # Ensure the destination directory exists
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        # Use the provided repo_name
        destination_path = os.path.join(destination_dir, repo_name)

        # Clone the GitHub repository to the specified path
        if os.path.exists(destination_path):  # Check if directory already exists
            return {"error": f"Directory {destination_path} already exists."}

        clone_command = ["git", "clone", github_url, destination_path]
        result = subprocess.run(clone_command, capture_output=True, text=True, check=True)
        return {"message": f"Repository cloned to {destination_path}", "output": result.stdout.strip()}
    except subprocess.CalledProcessError as e:
        return {"error": f"Failed to clone repository: {e.stderr.strip()}"}

# Build a Docker image from the cloned repository
def build_image_from_repo(github_url: str, image_name: str, repo_name: str):
    try:
        # Clone the repository first
        clone_response = clone_github_repo(github_url, repo_name)
        if "error" in clone_response:
            return clone_response  # Return error if cloning fails

        # Assuming the repository contains a Dockerfile at the root level
        destination_dir = os.path.join("/home/ubuntu", repo_name)  # Path where the repo is cloned

        # Build the Docker image
        build_command = ["docker", "build", "-t", image_name, destination_dir]

        # Run the build command
        build_response = run_command(build_command)
        return build_response
    except Exception as e:
        return {"error": str(e)}