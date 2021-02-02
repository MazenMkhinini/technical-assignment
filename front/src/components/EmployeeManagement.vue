<template>
  <div class="w-full max-w-screen-xl mx-auto p-6">
    <div
      class="relative rounded overflow-hidden border-grey-light mb-8 bg-white"
    >
      <div class="border-b border-grey-light p-4 bg-grey-lighter py-8">
        <div
          class="bg-white mx-auto max-w-sm shadow-lg rounded-lg overflow-hidden"
        >
          <div class="sm:flex sm:items-center px-2 py-4">
            <div class="flex-grow">
              <h3 class="font-normal px-2 py-3 leading-tight">Employees</h3>
              <input
                type="text"
                @input="(e) => textChanged(e.target.value)"
                placeholder="Search teams or members"
                class="my-2 w-full text-sm bg-grey-light text-grey-darkest rounded h-10 p-3 focus:outline-none"
              />
              <div class="w-full">
                <div
                  v-for="employee in employees"
                  :key="employee.id"
                  class="flex cursor-pointer my-1 hover:bg-blue-lightest rounded"
                  :data-id="id"
                  @drag="()=>{}"
                >
                  <div class="w-8 h-10 text-center py-1">
                    <p class="text-3xl p-0 text-green-dark">&bull;</p>
                  </div>
                  <div class="w-3/5 h-10 py-3 px-1">
                    <p class="hover:text-blue-dark">
                      {{ employee.first_name + " " + employee.last_name }}
                    </p>
                  </div>
                  <div class="w-1/5 h-10 text-right p-3">
                    <p class="text-sm text-grey-dark">{{ employee.role }}</p>
                  </div>
                  <div class="w-1/5 h-10 text-right p-3">
                    <img
                      class="h-full hover:color-red-500"
                      @click="() => deleteEmployee(employee.id)"
                      :src="DeleteSvg"
                    />
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="flex bg-grey-light sm:items-center px-2 py-4">
            <div class="flex-grow flex justify-center text-right items-center">
              <button
                class="bg-blue-500 flex inline-block justify-center items-center w-1/3 text-white px-3 py-2 rounded-md focus:outline-none"
                @click="showModal"
              >
                Add
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div
    v-if="employeeModalVisible"
    class="h-screen w-screen bg-opacity-40 bg-black fixed flex flex-col items-center justify-center"
  >
    <div class="h-screen w-full absolute flex items-center justify-center">
      <div class="flex flex-col justify-center sm:py-12">
        <div class="relative py-3 sm:max-w-xl sm:mx-auto">
          <div
            class="relative px-4 py-10 bg-white mx-8 md:mx-0 shadow rounded-3xl sm:p-10"
          >
            <div class="max-w-md mx-auto">
              <div class="flex items-center space-x-5">
                <div
                  class="block pl-2 font-semibold text-xl self-start text-gray-700"
                >
                  <h2 class="leading-relaxed">Add Employee</h2>
                </div>
              </div>
              <div class="divide-y divide-gray-200">
                <div
                  class="py-8 text-base leading-6 space-y-4 text-gray-700 sm:text-lg sm:leading-7"
                >
                  <div class="flex flex-col">
                    <label class="leading-loose">First Name</label>
                    <input
                      type="text"
                      v-model="firstName"
                      class="px-4 py-2 border focus:ring-gray-500 focus:border-gray-900 w-full sm:text-sm border-gray-300 rounded-md focus:outline-none text-gray-600"
                      placeholder="First Name"
                    />
                  </div>
                  <div class="flex flex-col">
                    <label class="leading-loose">Last Name</label>
                    <input
                      type="text"
                      v-model="lastName"
                      class="px-4 py-2 border focus:ring-gray-500 focus:border-gray-900 w-full sm:text-sm border-gray-300 rounded-md focus:outline-none text-gray-600"
                      placeholder="Last Name"
                    />
                  </div>
                  <div class="flex flex-col">
                    <label class="leading-loose">Role</label>
                    <input
                      type="text"
                      v-model="role"
                      class="px-4 py-2 border focus:ring-gray-500 focus:border-gray-900 w-full sm:text-sm border-gray-300 rounded-md focus:outline-none text-gray-600"
                      placeholder="Role"
                    />
                  </div>
                </div>
                <div class="pt-4 flex items-center space-x-4">
                  <button
                    class="bg-blue-500 flex justify-center items-center w-full text-white px-4 py-3 rounded-md focus:outline-none"
                    @click="addEmployee"
                  >
                    Create
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, watch } from "vue";
import DeleteSvg from "../assets/delete.svg";
export default {
  name: "Employees",
  props: {},
  setup() {
    const employees = ref([]);
    const firstName = ref("");
    const lastName = ref("");
    const role = ref("");
    const employeeModalVisible = ref(false);
    const originalEmployees = ref([]);
    const searchText = ref("");
    function fetchData() {
      return fetch("http://localhost:8000/employee", {
        method: "get",
        headers: {
          "content-type": "application/json",
        },
      })
        .then((res) => res.json())
        .then((json) => {
          // set the response data
          employees.value = json.data;
          originalEmployees.value = json.data;
        });
    }

    function hideModal() {
      employeeModalVisible.value = false;
    }

    function showModal() {
      employeeModalVisible.value = true;
    }

    async function addEmployee() {
      await fetch("http://localhost:8000/employee/add", {
        method: "POST",
        body: JSON.stringify({
          first_name: firstName.value,
          last_name: lastName.value,
          role: role.value,
        }),
      });
      fetchData();
    }

    function textChanged(text) {
      searchText.value = text;
      employees.value = originalEmployees.value.filter((x) =>
        new RegExp(searchText.value).test(x.first_name + " " + x.last_name)
      );
      console.log(text);
    }

    async function deleteEmployee(id) {
      await fetch("http://localhost:8000/employee/" + id, { method: "DELETE" });
      fetchData();
    }

    onMounted(() => {
      fetchData();
    });

    return {
      employees,
      originalEmployees,
      deleteEmployee,
      addEmployee,
      employeeModalVisible,
      hideModal,
      showModal,
      DeleteSvg,
      textChanged,
      firstName,
      lastName,
      role,
    };
  },
};
</script>

<style scoped>
a {
  color: #42b983;
}
</style>
