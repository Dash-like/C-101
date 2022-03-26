import dropbox

class datatransfer:
    def __init__(self, accessToken):
        self.accessToken = accessToken
    def uploadFile(self, filefrom, fileto):
        dbx = dropbox.Dropbox(self.accessToken)
        with open(filefrom, 'rb') as f:
            dbx.files_upload(f.read(), fileto)
def main():
    accessToken = "sl.BEgVu9d1wUKXd_owXN06Z3adMkqW_vHiqhb8mJu5XAlDomjGwjiJIBDTVIxN8NGj3S8OCr5kJ2MUJ4lQ5pXRgjw2bxOx33iAI47Qejel2lpsc47AxVZmcqI3wfzojXlUMvO3GJ4"
    transferdata = datatransfer(accessToken)
    filefrom = "test.txt"
    fileto = "/Users/DELL/dropbox/"
    transferdata.uploadFile(filefrom, fileto)
if __name__ == "__main__":
    main()
