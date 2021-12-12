import json


class DbWriter:

    def __init__(self, pseudo, email, motdepasse):

        self.pseudo = pseudo
        self.email = email
        self.motdepasse = motdepasse

        with open("users.json", "w") as file:

            data = {
                "pseudo": self.pseudo,
                "email": self.email,
                "motdepasse": self.motdepasse
            }

            json.dump(data, file)
            file.close()
