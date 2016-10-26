import subprocess


def has_connection():
    website = "google.com"
    ping = subprocess.Popen(["ping", website], stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    out, error = ping.communicate()
    if 'Sent = 4, Received = 4' in out.decode('utf-8'):
        return True
    return False

if __name__ == '__main__':
    print(has_connection())
