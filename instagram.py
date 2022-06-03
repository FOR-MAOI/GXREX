import os
os.system('git pull')
if __name__ == "__main__":
        try:
                __import__("igku").checkin()
        except Exception as e:
                exit(str(e))
