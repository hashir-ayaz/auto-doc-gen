import requests
import zipfile
import os


def download_github_repo(owner, repo, branch="main", output_dir="repos"):
    """Download a public GitHub repository as a ZIP file and extract it."""
    url = f"https://api.github.com/repos/{owner}/{repo}/zipball/{branch}"
    try:
        print(f"Downloading {repo} from {url}...")
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            os.makedirs(output_dir, exist_ok=True)
            zip_path = os.path.join(output_dir, f"{repo}.zip")

            with open(zip_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)

            print(f"Extracting to {output_dir}...")
            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                zip_ref.extractall(output_dir)

            os.remove(zip_path)  # Cleanup
            print(f"Repository {repo} downloaded and extracted to {output_dir}.")
        else:
            print(f"Failed to download repository. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")


# Example usage
owner = "mahaamimran"
repo = "dei_marc"
download_github_repo(owner, repo)
