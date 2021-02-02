<template>
  <div class="w-full max-w-screen-xl mx-auto p-6">
    <div
      class="relative rounded overflow-hidden border-grey-light mb-8 bg-white"
    >
      <div class="border-b border-grey-light p-4 bg-grey-lighter py-8">
        <div
          class="bg-white shadow-lg rounded-lg overflow-hidden"
        >
          <div class="sm:flex sm:items-center px-2 py-4">
            <div class="flex-grow">
              <h3 class="font-normal px-2 py-3 leading-tight">Timeslots</h3>
              <div class="w-full">
                <div
                  v-for="timeslot in timeslots"
                  :key="timeslot.id"
                  class="flex cursor-pointer my-1 hover:bg-blue-lightest rounded"
                >
                  <div class="w-8 h-10 text-center py-1">
                    <p class="text-3xl p-0 text-green-dark">&bull;</p>
                  </div>
                  <div class="w-2/5 h-10 py-3 px-1">
                    <p class="hover:text-blue-dark">
                      {{ timeslot.start }}
                    </p>
                  </div>
                  <div class="w-2/5 h-10 text-right p-3">
                    <p class="text-sm text-grey-dark">{{ timeslot.end }}</p>
                  </div>
                  <div class="w-1/5 h-10 text-right p-3">
                    <img
                      class="h-full hover:color-red-500"
                      @click="() => deletetimeslot(timeslot.id)"
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
    v-if="timeslotModalVisible"
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
                  <h2 class="leading-relaxed">Add timeslot</h2>
                </div>
              </div>
              <div class="divide-y divide-gray-200">
                <div
                  class="py-8 text-base leading-6 space-y-4 text-gray-700 sm:text-lg sm:leading-7"
                >
                  <div class="flex flex-col">
                    <label class="leading-loose">Start</label>
                    <input
                      type="datetime-local"
                      v-model="start"
                      class="px-4 py-2 border focus:ring-gray-500 focus:border-gray-900 w-full sm:text-sm border-gray-300 rounded-md focus:outline-none text-gray-600"
                      placeholder="Start"
                    />
                  </div>
                  <div class="flex flex-col">
                    <label class="leading-loose">End</label>
                    <input
                      type="datetime-local"
                      v-model="end"
                      class="px-4 py-2 border focus:ring-gray-500 focus:border-gray-900 w-full sm:text-sm border-gray-300 rounded-md focus:outline-none text-gray-600"
                      placeholder="End"
                    />
                  </div>
                </div>
                <div class="pt-4 flex items-center space-x-4">
                  <button
                    class="bg-blue-500 flex justify-center items-center w-full text-white px-4 py-3 rounded-md focus:outline-none"
                    @click="addTimeslot"
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
  name: "timeslots",
  props: {},
  setup() {
    const timeslots = ref([]);
    const role = ref("");
    const start = ref("");
    const end = ref("");
    const timeslotModalVisible = ref(false);
    const originalTimeslots = ref([]);
    const searchText = ref("");
    function fetchData() {
      return fetch("http://localhost:8000/timeslot", {
        method: "get",
        headers: {
          "content-type": "application/json",
        },
      })
        .then((res) => res.json())
        .then((json) => {
          // set the response data
          timeslots.value = json.data;
          originalTimeslots.value = json.data;
        });
    }

    function hideModal() {
      timeslotModalVisible.value = false;
    }

    function showModal() {
      timeslotModalVisible.value = true;
    }

    async function addTimeslot() {
      await fetch("http://localhost:8000/timeslot/add", {
        method: "POST",
        body: JSON.stringify({
          start: start.value,
          end: end.value,
        }),
      });
      fetchData();
    }

    function textChanged(text) {
      searchText.value = text;
      timeslots.value = originalTimeslots.value.filter((x) =>
        new RegExp(searchText.value).test(x.first_name + " " + x.last_name)
      );
      console.log(text);
    }

    async function deletetimeslot(id) {
      await fetch("http://localhost:8000/timeslot/" + id, { method: "DELETE" });
      fetchData();
    }

    onMounted(() => {
      fetchData();
    });

    return {
      timeslots,
      originalTimeslots,
      deletetimeslot,
      addTimeslot,
      timeslotModalVisible,
      hideModal,
      showModal,
      DeleteSvg,
      CancelSvg,
      textChanged,
      start,
      end,
      role,
      start,
      end,
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
