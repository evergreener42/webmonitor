import subprocess

def run_linux_command(command):
    try:
        # Execute the Linux command
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        # Print the output (stdout and stderr)
        print("Command output:")
        print(result.stdout)
        print("Error (if any):")
        print(result.stderr)
    except Exception as e:
        print(f"Error executing the command: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with your actual Linux command
    my_linux_command = "ls -l /path/to/directory"
    
    run_linux_command(my_linux_command)
