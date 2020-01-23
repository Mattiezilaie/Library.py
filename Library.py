# Author: Mahtab Zilaie
# Date: January 22 2020
# Description: Library simulator that checks out patrons and returns fine amount for
# overdue books.


class LibraryItem:

    """two data members id_code and title"""

    def __init__(self, id_code, title):
        """initializes id code, title, location, checked_out_by requested by, and date checked out"""
        self._id_code = id_code
        self._title = title
        self._location = "ON_SHELF"
        self._checked_out_by = None
        self._requested_by = None
        self.date_checked_out = 0

    def get_id_code(self):
        return self._id_code

    def get_title(self):
        return self._title

    def set_location(self, location):
        self._location = location

    def get_location(self):
        return self._location

    def set_checked_out_by(self, patron):
        self._checked_out_by = patron

    def get_checked_out_by(self):
        return self._checked_out_by

    def set_requested_by(self, patron):
        self._requested_by = patron

    def get_requested_by(self):
        return self._requested_by

    def set_date_checked_out(self, day):
        self.date_checked_out = day

    def get_date_checked_out(self):
        return self.date_checked_out


class Book(LibraryItem):

    """id code, title, and author three data members in book class which inherits from LibraryItm"""

    def __init__(self, id_code, title, author):

        """initializes author """

        super().__init__(id_code, title)
        self._author = author

    def get_check_out_length(self):
        return 21

    def get_author(self):
        return self._author


class Album(LibraryItem):

    """inherits id_code and title from LibraryItem"""
    def __init__(self, id_code, title, artist):

        """initializes artist"""

        super().__init__(id_code, title)
        self._artist = artist

    def get_check_out_length(self):
        return 14

    def get_artist(self):
        return self._artist


class Movie(LibraryItem):

    """inherits id_code and title from LibraryItem"""

    def __init__(self, id_code, title, director):

        """initializes director"""

        super().__init__(id_code, title)
        self._director = director

    def get_check_out_length(self):
        return 7

    def get_director(self):
        return self._director


class Patron:

    """data members id_num and name"""

    def __init__(self, id_num, name):

        """initialzes idnum, name, checked out items to list, and fine_amount"""

        self._id_num = id_num
        self._name = name
        self._checked_out_items = []
        self.fine_amount = 0

    def set_fine_amount(self, amount):
        """sets fine amount to data member amount"""
        self.fine_amount = amount

    def set_checked_out_items(self, item):
        """adds item to check_out_items list"""
        self._checked_out_items.append(item)

    def get_checked_out_items(self):
        """returns checked_out items list"""
        return self._checked_out_items

    def get_id_num(self):
        """returns id_num"""
        return self._id_num

    def get_name(self):
        """returns name"""
        return self._name

    def add_library_item(self, lib_item):
        """adds lib_item to add_library_item list"""
        self._checked_out_items.append(lib_item)

    def remove_library_item(self, lib_item):
        """adds lib_item to remove_library_item list"""
        self._checked_out_items.remove(lib_item)

    def get_fine_amount(self):
        """returns fine amount"""
        return self.fine_amount

    def amend_fine(self, num):
        """selfs fin_amount to fine_amount plus data member num"""
        self.fine_amount = self.fine_amount + num

class Library:

    """library class with no data members"""

    def __init__(self):

        """initializes current_date, holdings, members and lib"""
        self._current_date = 0
        self._holdings = []
        self._members = []
        self.lib = None

    def set_holdings(self, item):
        """adds item to holdings"""
        self._holdings.append(item)

    def set_members(self,member):
        """adds member to members list"""
        self._members.append(member)

    def get_members(self):
        """returns member"""
        return self._members

    def set_current_date(self, day):
        """sets current_date to day"""
        self._current_date = day

    def get_current_date(self):
        """returns current date"""
        return self._current_date

    def add_library_item(self, library_item):
        """adds library item to holdings list"""
        self._holdings.append(library_item)

    def add_patron(self, patron_name):
        """adds patron name to members list"""
        self._members.append(patron_name)

    def get_library_item(self, id_item):  #returns the LibraryItem corresponding to the ID
        for item in self._holdings:
            if id_item == item.get_id_code():
                return item
        return None

    def get_patron(self, id_patron):  #returns the Patron corresponding to the ID
        for persons in self._members:
            if id_patron == persons.get_id_num():
                return persons
        return None

    def check_out_library_item(self, patron_id, item_id):
        if self.get_library_item(item_id) is None: #if the specified LibraryItem is not in the Library's
            return "item not found"                   # holdings

        if self.get_patron(patron_id) is None:
            return "patron not found"   #specified Patron is not in the Library's members
        # Situation if library item is already checked out:
        libs = self.get_library_item(item_id)
        if libs.get_location() == "CHECKED_OUT":
            return "item already checked out"

        if libs.get_location() == "ON_HOLD_SHELF" and libs.get_requested_by() != patron_id:
            return "item on hold by other patron"
        LibraryItem.set_checked_out_by(self, patron_id) #update the LibraryItem's checkedOutBy
        libs.set_date_checked_out(self._current_date) #update dateCheckedOut
        libs.set_location("CHECKED_OUT")

        if libs.get_requested_by() == patron_id:
            libs.set_requested_by(None)   # update requestedBy
        pat = Library.get_patron(self, patron_id)
        pat.add_library_item(item_id)
        return "check out successful"

    def return_library_item(self, item_id):

        Lib = LibraryItem(self, item_id)
        if item_id not in self._holdings:
            return "item not found"  # specified LibraryItem is not in the Library's holdings, return "item not found"

        elif Lib.get_location() != "CHECKED OUT":
            return "item already in library"  # LibraryItem is not checked out, returns "item already in library"
        Patron.checked_out_items(self, item_id)  # updates the Patron's checkedOutItems

        if Lib.get_requested_by() != None:
            Lib.set_location("ON_HOLD_SHELF")

        LibraryItem.set_checked_out_by(None)  # update the LibraryItem's checkedOutBy
        return "return successful"

    def request_library_item(self, item_id, patron_id):
        if item_id not in self._holdings:  # specified LibraryItem is not in the Library's holdings
            return "item not found"
        if patron_id not in self._members:  # specified Patron is not in the Library's members
            return "patron not found"
        if LibraryItem.get_location(item_id) == "ON_HOLD_SHELF":  # specified LibraryItem is already requested
            return "item already on hold"
        LibraryItem.set_requested_by(patron_id)  # update the LibraryItem's requestedBy

        if LibraryItem.get_location(item_id) == "ON_SHELF":  # if the LibraryItem is on the shelf
            item_id.set_location("ON_HOLD_SHELF")  # update its location to on hold
            return "request successful"

    def pay_fine(self, patron_id, amount_paid):
        if patron_id not in self._holdings:  # specified Patron is not in the Library's members
            return "patron not found"
        Patron.amend_fine(amount_paid)
        return "payment successful"

    def increment_current_date(self):
        self._current_date += 1  # increment current date by 1

        for member in self._members:
            for i in member.get_checked_out_items():
                if Library.get_current_date < i.date_checked_out():
                    over_due = i.date_checked_out() - i.get_current_date()
                    for i in range(over_due + 1):
                        member.append_fine(over_due * .1)