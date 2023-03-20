"""
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



mlm = MLM("Alice")



# Sidebar for adding members


st.sidebar.subheader("Add Members")


sponsor_name = st.sidebar.text_input("Enter sponsor name")


member_name = st.sidebar.text_input("Enter member name")


if st.sidebar.button("Add member"):


    mlm.add_member(sponsor_name, member_name)



# Sidebar for updating points


st.sidebar.subheader("Update Points")


member_name = st.sidebar.text_input("Enter member name")


points = st.sidebar.number_input("Enter points", min_value=0, step=1)


if st.sidebar.button("Update points"):


    mlm.update_points(member_name, points)



# Main content


st.header("MLM Network")
mlm.print_members()


#streamlit run full_mlm.py


"""


"""The given code is an implementation of Multi-level Marketing (MLM) using Python classes. MLM is a business model in which members promote and sell products or services, and they also recruit new members to join the MLM network.



The code defines two classes: Member and MLM. The Member class represents a single member in the MLM network. Each member has a name, a sponsor (i.e., the member who introduced them to the MLM network), a left and a right member (i.e., their downline members in the MLM network), a level (i.e., the depth of the member in the MLM network), and a number of points that they have earned.



The MLM class represents the entire MLM network. It has a root member (i.e., the first member who joined the MLM network), and it provides methods to add new members to the network, update their points, find members by name, and print the entire network.



The code starts by creating an MLM network with the root member named "Alice". It then adds four more members to the network: "Bob" and "Charlie" under "Alice", and "Dave" and "Eve" under "Bob" and "Charlie" respectively.



After that, it updates the points earned by "Bob" and "Eve" by calling the update_points() method of the MLM class. Finally, it prints the entire MLM network using the print_members() method of the MLM class.



In the Streamlit implementation, the user is asked to enter the names of the members and their sponsors, and the number of points they have earned. The network is then created and displayed to the user. The user can update the points earned by any member and see the updated network."""

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




mlm = MLM("Alice")



# Add members


col1, col2 = st.columns(2)


with col1:


    sponsor_name = st.text_input("Sponsor Name",key=" sponsor_name")


with col2:


    member_name2 = st.text_input("Member Name",key=" member_name2")



if st.button("Add Member"):


    mlm.add_member(sponsor_name, member_name2)



# Update member points


col1, col2 = st.columns(2)


with col1:


    member_name1 = st.text_input("Member Name",key=" member_name1")


with col2:


    points = st.number_input("Points", min_value=0)



if st.button("Update Points"):


    mlm.update_points(member_name, points)



# Print members


st.write("## Members")
mlm.print_members()


#streamlit run full_mlm.py