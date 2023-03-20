#python
"""
class Member:
    def __init__(self, name, sponsor=None):
        self.name = name
        self.sponsor = sponsor
        self.left = None
        self.right = None
        self.level = 0
        self.points = 0

    def add_member(self, member):
        if self.left is None:
            self.left = member
            self.left.sponsor = self
            self.left.level = self.level + 1
        elif self.right is None:
            self.right = member
            self.right.sponsor = self
            self.right.level = self.level + 1
        else:
            print("Both legs are occupied")

    def get_points(self):
        return self.points

    def update_points(self, points):
        self.points += points
        if self.sponsor is not None:
            self.sponsor.update_points(points)

    def __str__(self):
        return f"{self.name} ({self.points} points)"


class MLM:
    def __init__(self, root_name):
        self.root = Member(root_name)

    def add_member(self, sponsor_link, member_name):
        sponsor = self.find_member(self.root, sponsor_link)
        if sponsor is not None:
            member = Member(member_name)
            sponsor.add_member(member)
        else:
            print("Sponsor not found")

    def find_member(self, member, link):
        if member is None:
            return None
        elif id(member) == link:
            return member
        else:
            left_result = self.find_member(member.left, link)
            if left_result is not None:
                return left_result
            else:
                return self.find_member(member.right, link)

    def get_members_at_level(self, level):
        members = []
        self.get_members_at_level_helper(self.root, level, members)
        return members

    def get_members_at_level_helper(self, member, level, members):
        if member is None:
            return
        elif member.level == level:
            members.append(member)
        else:
            self.get_members_at_level_helper(member.left, level, members)
            self.get_members_at_level_helper(member.right, level, members)

    def update_points(self, member_link, points):
        member = self.find_member(self.root, member_link)
        if member is not None:
            member.update_points(points)
        else:
            print("Member not found")

    def print_members(self):
        self.print_members_helper(self.root)

    def print_members_helper(self, member):
        if member is None:
            return
        self.print_members_helper(member.left)
        print(member)
        self.print_members_helper(member.right)


mlm = MLM("Alice")
bob = Member("Bob")
mlm.root.left = bob
bob.sponsor = mlm.root
bob.level = 1
charlie = Member("Charlie")
mlm.root.right = charlie
charlie.sponsor = mlm.root
charlie.level = 1
dave = Member("Dave")
bob.left = dave
dave.sponsor = bob
dave.level = 2
eve = Member("Eve")
charlie.right = eve
eve.sponsor = charlie
eve.level = 2

mlm.update_points(id(bob), 100)
mlm.update_points(id(eve), 50)

mlm.print_members()

another one 
class Member:
    def __init__(self, name, sponsor=None):
        self.name = name
        self.sponsor = sponsor
        self.left = None
        self.right = None
        self.level = 0
        self.points = 0

    def add_member(self, member):
        if self.left is None:
            self.left = member
            self.left.sponsor = self
            self.left.level = self.level + 1
        elif self.right is None:
            self.right = member
            self.right.sponsor = self
            self.right.level = self.level + 1
        else:
            print("Both legs are occupied")

    def get_points(self):
        return self.points

    def update_points(self, points):
        self.points += points
        if self.sponsor is not None:
            self.sponsor.update_points(points)

    def __str__(self):
        return f"{self.name} ({self.points} points)"


class MLM:
    def __init__(self, root_name):
        self.root = Member(root_name)

    def add_member(self, sponsor_name, member_name):
        sponsor = self.find_member(self.root, sponsor_name)
        if sponsor is not None:
            member = Member(member_name)
            sponsor.add_member(member)
        else:
            print("Sponsor not found")

    def find_member(self, member, name):
        if member is None:
            return None
        elif member.name == name:
            return member
        else:
            left_result = self.find_member(member.left, name)
            if left_result is not None:
                return left_result
            else:
                return self.find_member(member.right, name)

    def get_members_at_level(self, level):
        members = []
        self.get_members_at_level_helper(self.root, level, members)
        return members

    def get_members_at_level_helper(self, member, level, members):
        if member is None:
            return
        elif member.level == level:
            members.append(member)
        else:
            self.get_members_at_level_helper(member.left, level, members)
            self.get_members_at_level_helper(member.right, level, members)

    def update_points(self, member_name, points):
        member = self.find_member(self.root, member_name)
        if member is not None:
            member.update_points(points)
        else:
            print("Member not found")

    def print_members(self):
        self.print_members_helper(self.root)

    def print_members_helper(self, member):
        if member is None:
            return
        self.print_members_helper(member.left)
        print(member)
        self.print_members_helper(member.right)


mlm = MLM("Alice")
mlm.add_member("Alice", "Bob")
mlm.add_member("Alice", "Charlie")
mlm.add_member("Bob", "Dave")
mlm.add_member("Charlie", "Eve")

mlm.update_points("Bob", 100)
mlm.update_points("Eve", 50)

mlm.print_members()
"""
"""The code defines two classes, Member and MLM. Each Member object represents a member in the MLM, and each MLM object represents the MLM itself. The Member class has attributes such as name, sponsor, left, and right, which represent the member's name, their sponsor, and the members they have recruited in their left and right legs. Each"""
#streamlit 
import streamlit as st


class Member:
    def __init__(self, name, sponsor=None):
        self.name = name
        self.sponsor = sponsor
        self.left = None
        self.right = None
        self.level = 0
        self.points = 0

    def add_member(self, member):
        if self.left is None:
            self.left = member
            self.left.sponsor = self
            self.left.level = self.level + 1
        elif self.right is None:
            self.right = member
            self.right.sponsor = self
            self.right.level = self.level + 1
        else:
            st.warning("Both legs are occupied")

    def get_points(self):
        return self.points

    def update_points(self, points):
        self.points += points
        if self.sponsor is not None:
            self.sponsor.update_points(points)

    def __str__(self):
        return f"{self.name} ({self.points} points)"


class MLM:
    def __init__(self, root_name):
        self.root = Member(root_name)

    def add_member(self, sponsor_name, member_name):
        sponsor = self.find_member(self.root, sponsor_name)
        if sponsor is not None:
            member = Member(member_name)
            sponsor.add_member(member)
            st.success(f"Added {member_name} to {sponsor_name}")
        else:
            st.warning("Sponsor not found")

    def find_member(self, member, name):
        if member is None:
            return None
        elif member.name == name:
            return member
        else:
            left_result = self.find_member(member.left, name)
            if left_result is not None:
                return left_result
            else:
                return self.find_member(member.right, name)

    def get_members_at_level(self, level):
        members = []
        self.get_members_at_level_helper(self.root, level, members)
        return members

    def get_members_at_level_helper(self, member, level, members):
        if member is None:
            return
        elif member.level == level:
            members.append(member)
        else:
            self.get_members_at_level_helper(member.left, level, members)
            self.get_members_at_level_helper(member.right, level, members)

    def update_points(self, member_name, points):
        member = self.find_member(self.root, member_name)
        if member is not None:
            member.update_points(points)
            st.success(f"Updated {member_name}'s points to {member.get_points()}")
        else:
            st.warning("Member not found")

    def print_members(self):
        self.print_members_helper(self.root)

    def print_members_helper(self, member):
        if member is None:
            return
        self.print_members_helper(member.left)
        st.write(member)
        self.print_members_helper(member.right)


def run():
    st.title("Multi-Level Marketing")

    mlm = MLM("Alice")

    # Add member form
    st.header("Add a member")
    sponsor_name = st.text_input("Sponsor name")
    member_name = st.text_input("Member name")
    if st.button("Add member"):
        mlm.add_member(sponsor_name, member_name)

    # Update points form
    st.header("Update points")
    member_name = st.text_input("Member name")
    points = st.number_input("Points", value=0)
    if st.button("Update points"):
        mlm.update_points(member_name, points)

    # Display members
    st.header("Members")
    mlm.print_members()


if __name__ == '__':


#streamlit run mlm_implementation.py