class iPhone:
    def __init__(self, user_name, phone_name, phone_number):
        self.user_name = user_name
        self.phone_name = phone_name
        self.phone_number = phone_number
        self.inbox = []

    def set_name(self):
        print(f"Your current iPhone name is: {self.phone_name}")
        new_phone_name = input(f"Set a new iPhone name: ")
        self.phone_name = new_phone_name
        pass

    def show_name(self):
        print(self.phone_name)
        pass

    def send_imessage(self, receiver):
        new_message = input(f"iMessage to {receiver.user_name}, {receiver.phone_number}: ")
        receiver.inbox.append(f"From {self.user_name}: {new_message}")
        pass

    def check_inbox(self):
        if self.inbox:
            print(f"Messages for {self.user_name}:")
            for message in self.inbox:
                print(f"\t{message}")
        else:
            print(f"No messages for {self.user_name}")
        pass


phone1 = iPhone("Marjorie", "Marjorie's Phone", "123-123-1234")
phone2 = iPhone("Ian", "Ian's Phone", "123-123-1235")

phone1.set_name()
phone1.show_name()
phone1.send_imessage(phone2)
phone2.check_inbox()