<template>
  
</template>

<script>
import { ref, onMounted, watch } from "vue";
import DeleteSvg from "../assets/delete.svg";
export default {
  name: "Employees",
  props: {},
  setup() {
    const employees = ref([]);
    const timeslots = ref([]);
    const timeslotsOccupation  = ref ([]);
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
          timeslots.value = json.data;
        });
    }

    async function addTimeslotOccupation() {
      await fetch("http://localhost:8000/timeslot_occupation/add", {
        method: "POST",
        body: JSON.stringify({
          first_name: firstName.value,
          last_name: lastName.value,
          role: role.value,
        }),
      });
      fetchData();
    }

    async function deleteTimeslotOccupation(id) {
      await fetch("http://localhost:8000/timeslot_occupation/" + id, { method: "DELETE" });
      fetchData();
    }

    onMounted(() => {
      fetchData();
    });

    return {
      employees,
      timeslots,
      timeslotsOccupation,
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
</style>
