import subprocess

def restore_postgres(database_name, user, password, host, port, backup_file):
    try:
        # Set the environment variable for the password
        env = {"PGPASSWORD": password}

        # Command for a plain SQL dump
        command = [
            "pg_restore",
            "-h", host,
            "-p", str(port),
            "-U", user,
            "-d", database_name,
            "-f", backup_file
        ]

        # Run the command and capture output
        result = subprocess.run(command, env=env, capture_output=True, text=True, check=True)
        print("Database restored successfully.")
    except subprocess.CalledProcessError as e:
        print("Error restoring database:")
        print(e.stderr)  # Display the error details
