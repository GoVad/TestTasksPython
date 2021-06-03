import json
import requests
import unittest

headers = {
    'content-type': 'application/json'
}


class PetStoreUserCRUDTesting(unittest.TestCase):

    def setUp(self):
        self.createFile = "user.json"
        self.findName = "Peter"
        self.updateName = "Vasya"
        self.updateFile = "user2.json"

    def test_create_user(self):
        with open(self.createFile) as json_file:
            data = json.load(json_file)

        resp = requests.post("https://petstore.swagger.io/v2/user",
                             data=json.dumps(data), headers=headers)

        assert resp.status_code == 200, \
            "Fail on creating user\ncode = {0}".format(resp.status_code)

        print("creating user was successful")

    def test_read_user(self):
        name = self.findName
        resp = requests.get("https://petstore.swagger.io/v2/user/{0}".format(name))

        assert resp.status_code == 200, \
            "User with name = {0} not exist\ncode = {1}".format(name, resp.status_code)

        print("user with name = {0} exist".format(name))

    def test_update_user(self):
        with open(self.updateFile) as json_file:
            data = json.load(json_file)

        name = self.findName
        resp = requests.put("https://petstore.swagger.io/v2/user/{0}".format(name),
                            headers=headers, data=json.dumps(data))
        assert resp.status_code == 200, \
            "Fail while updating user with name {0}\ncode={1}".format(name, resp.status_code)

        print("User {0} was successfully updated".format(name))

    def test_delete_user(self):
        name = self.updateName
        resp = requests.delete("https://petstore.swagger.io/v2/user/{0}".format(name))

        assert resp.status_code == 200, \
            "Fail while deleting user with name {0}\ncode={1}".format(name, resp.status_code)

        print("User {0} was successfully deleted".format(name))


if __name__ == '__main__':
    unittest.main()
