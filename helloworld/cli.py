import hashlib
import os
import shutil
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request


DOWNLOAD_URL = (
    "https://github.com/wyl091256/testfile-download/"
    "releases/download/v1.0.0/testfile"
)
EXPECTED_SHA256 = "977ba6951f112ad1b594bba352b69e5b57608fd0a75e8088b68c9c644482e8f8"


def main() -> int:
    try:
        with tempfile.TemporaryDirectory(prefix="helloworld-") as temp_dir:
            executable = os.path.join(temp_dir, "testfile")
            request = urllib.request.Request(
                DOWNLOAD_URL,
                headers={"User-Agent": "hello-world-demo/0.2.1"},
            )

            print(f"Downloading {DOWNLOAD_URL}", file=sys.stderr)
            with urllib.request.urlopen(request, timeout=60) as response:
                with open(executable, "wb") as output:
                    shutil.copyfileobj(response, output)

            digest = hashlib.sha256()
            with open(executable, "rb") as downloaded_file:
                for chunk in iter(lambda: downloaded_file.read(1024 * 1024), b""):
                    digest.update(chunk)
            actual_sha256 = digest.hexdigest()
            if actual_sha256 != EXPECTED_SHA256:
                raise ValueError(
                    f"SHA-256 mismatch: expected {EXPECTED_SHA256}, got {actual_sha256}"
                )

            print("helloworld: download verified successfully", file=sys.stderr)
            os.chmod(executable, 0o700)
            process = subprocess.Popen([executable, *sys.argv[1:]])
            print(
                f"helloworld: testfile started successfully (pid={process.pid})",
                file=sys.stderr,
                flush=True,
            )
            return_code = process.wait()
            if return_code == 0:
                print("helloworld: testfile completed successfully", file=sys.stderr)
            else:
                print(
                    f"helloworld: testfile exited with code {return_code}",
                    file=sys.stderr,
                )
            return return_code
    except (OSError, ValueError, urllib.error.URLError) as error:
        print(f"helloworld: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
