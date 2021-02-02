<template>
  <div class="antialiased font-sans">
    <div class="container mx-auto px-4 sm:px-8">
      <div class="py-8">
        <div class="-mx-4 sm:-mx-8 px-4 sm:px-8 py-4 overflow-x-auto">
          <div
            class="inline-block min-w-full shadow rounded-lg overflow-hidden"
          >
            <table class="min-w-full leading-normal">
              <thead>
                <tr>
                  <th
                    class="px-5 py-3 border-b-2 border-gray-200 bg-gray-100 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider"
                  >
                    Employee
                  </th>
                  <th
                    class="px-5 py-3 border-b-2 border-gray-200 bg-gray-100 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider"
                  >
                    Timeslot
                  </th>
                  <th
                    class="px-5 py-3 border-b-2 border-gray-200 bg-gray-100 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider"
                  >
                    Delete
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="to in timeslotsOccupation" :key="to.id">
                  <td
                    class="px-5 py-5 border-b border-gray-200 bg-white text-sm"
                  >
                    <div class="flex items-center">
                      <div class="ml-3">
                        <p class="text-gray-900 whitespace-no-wrap">
                          {{ to.employee }}
                        </p>
                      </div>
                    </div>
                  </td>
                  <td
                    class="px-5 py-5 border-b border-gray-200 bg-white text-sm"
                  >
                    <p class="text-gray-900 whitespace-no-wrap">
                      {{ to.timeslot }}
                    </p>
                  </td>
                  <td>
                    <div class="flex w-full justify-center">
                      <img 
                      @click="()=>deleteTimeslotOccupation(to.id)"
                      class="h-5" :src="DeleteSvg" alt="" />
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
            <div
              class="px-5 py-5 bg-white border-t flex flex-col xs:flex-row items-center xs:justify-between"
            >
              <div class="inline-flex mt-2 xs:mt-0">
                <button
                  @click="showModal"
                  class="bg-blue-500 text-white font-semibold py-2 px-4 rounded"
                >
                  Add
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div
    v-if="timeslotOccupationModalVisible"
    class="h-screen w-screen bg-opacity-40 bg-black fixed flex flex-col items-center justify-center"
  >
    <div class="h-screen w-full absolute flex items-center justify-center">
      <div class="flex flex-col justify-center sm:py-12">
        <div class="relative py-3 sm:max-w-xl sm:mx-auto">
          <div
            class="relative px-4 py-10 bg-white mx-8 md:mx-0 shadow rounded-3xl sm:p-10"
          >
            <img
              :src="CancelSvg"
              alt=""
              @click="hideModal"
              class="absolute w-5 h-5 cursor-pointer position-custom"
            />
            <div class="max-w-md mx-auto">
              <div class="flex items-center space-x-5">
                <div
                  class="block pl-2 font-semibold text-xl self-start text-gray-700"
                >
                  <h2 class="leading-relaxed">Affect employee to timeslot</h2>
                </div>
              </div>
              <div class="divide-y divide-gray-200">
                <div
                  class="py-8 text-base leading-6 space-y-4 text-gray-700 sm:text-lg sm:leading-7"
                >
                  <div class="flex flex-col">
                    <label class="leading-loose">Employee</label>
                    <select
                      v-model="employee"
                      class="px-4 py-2 border focus:ring-gray-500 focus:border-gray-900 w-full sm:text-sm border-gray-300 rounded-md focus:outline-none text-gray-600"
                    >
                      <option v-for="e in employees" :value="e.id">
                        {{ e.id }}
                      </option>
                    </select>
                  </div>
                </div>
                <div
                  class="py-8 text-base leading-6 space-y-4 text-gray-700 sm:text-lg sm:leading-7"
                >
                  <div class="flex flex-col">
                    <label class="leading-loose">Timeslot</label>
                    <select
                      v-model="timeslot"
                      class="px-4 py-2 border focus:ring-gray-500 focus:border-gray-900 w-full sm:text-sm border-gray-300 rounded-md focus:outline-none text-gray-600"
                    >
                      <option v-for="t in timeslots" :value="t.id">
                        {{ t.id }}
                      </option>
                    </select>
                  </div>
                </div>
                <div class="pt-4 flex items-center space-x-4">
                  <button
                    class="bg-blue-500 flex justify-center items-center w-full text-white px-4 py-3 rounded-md focus:outline-none"
                    @click="addTimeslotOccupation"
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
import CancelSvg from "../assets/cancel.svg";
export default {
  name: "Employees",
  props: {},
  setup() {
    const employees = ref([]);
    const employee = ref(null);
    const timeslot = ref(null);
    const timeslots = ref([]);
    const timeslotsOccupation = ref([]);
    const timeslotOccupationModalVisible = ref(false);

    function fetchData() {
      fetch("http://localhost:8000/employee", {
        method: "get",
        headers: {
          "content-type": "application/json",
        },
      })
        .then((res) => res.json())
        .then((json) => {
          // set the response data
          employees.value = json.data;
        });

      fetch("http://localhost:8000/timeslot", {
        method: "get",
        headers: {
          "content-type": "application/json",
        },
      })
        .then((res) => res.json())
        .then((json) => {
          // set the response data
          timeslots.value = json.data;
        });

      fetch("http://localhost:8000/timeslot_occupation", {
        method: "get",
        headers: {
          "content-type": "application/json",
        },
      })
        .then((res) => res.json())
        .then((json) => {
          // set the response data
          timeslotsOccupation.value = json.data;
        });
    }

    async function addTimeslotOccupation() {
      await fetch("http://localhost:8000/timeslot_occupation/add", {
        method: "POST",
        body: JSON.stringify({
          employee: employee.value,
          timeslot: timeslot.value,
        }),
      });
      fetchData();
      hideModal();
    }

    function hideModal() {
      timeslotOccupationModalVisible.value = false;
    }

    function showModal() {
      timeslotOccupationModalVisible.value = true;
    }

    async function deleteTimeslotOccupation(id) {
      await fetch("http://localhost:8000/timeslot_occupation/" + id, {
        method: "DELETE",
      });
      fetchData();
    }

    onMounted(() => {
      fetchData();
    });

    return {
      employees,
      timeslots,
      timeslotOccupationModalVisible,
      hideModal,
      showModal,
      employee,
      timeslot,
      timeslotsOccupation,
      DeleteSvg,
      CancelSvg,
      deleteTimeslotOccupation,
      addTimeslotOccupation,
    };
  },
};
</script>

<style scoped>
a {
  color: #42b983;
}

.position-custom {
  top: 10px;
  right: 10px;
}
</style>
