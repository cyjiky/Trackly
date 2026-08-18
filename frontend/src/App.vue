<template>
  <Navigation />

  <div className="container">
    <div className="container-head">
      <p className="title">Your tasks today: </p>
      <AddButton/>
    </div>
    <Checkbox 
      v-for="task in tasks"
      :key="task.id"
      :tasks="task"
    />
      <!-- <pre>{{ tasks }}</pre> -->
  </div>

  <Footer />
</template>

<script>
import Checkbox from './components/Checkbox.vue';
import AddButton from './components/AddButton.vue';
import Navigation from './components/Navigation.vue';
import Footer from './components/Footer.vue';

export default {
  name: 'Trackly-App',
  components: {
    Navigation,
    AddButton,
    Checkbox, 
    Footer
  },
  data () {
    return {
        tasks: []
    }
  },
  methods: {
    async getTaskFetch(path = 'http://127.0.0.1:8000/task') {
    try {
      const response = await fetch(path);

      if (!response.ok) {
        throw new Error(`status: ${response.status}`);
      }

      const data = await response.json();
      console.log(data);
      this.tasks = data;
      
    } catch (error) {
      console.error(error);
    }
    }
  },
  mounted() {
    this.getTaskFetch();
  }
}
</script>