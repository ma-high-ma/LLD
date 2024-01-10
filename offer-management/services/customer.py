from dao.customer import CustomerDao
from exceptions import CustomerNotFound


class CustomerService:
    def create_customer(self, name, dob, age):
        return CustomerDao().create(name, dob, age)

    def get_by_id(self, id):
        try:
            return CustomerDao().get_by_id(id)
        except CustomerNotFound as e:
            print("Error: ", str(e))
            return None
