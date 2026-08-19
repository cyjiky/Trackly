<template>
  <Navigation />

  <div className="container">
    <div className="container-head">
      <p className="title">Your tasks today: </p>
      <button className="custom-button" @click="openModal">+</button>
    </div>
    <Checkbox 
      v-for="task in tasks"
      :key="task.id"
      :tasks="task"
      @delete-task="deleteTaskfetch"
    />
    
    <ModalCard :showing="isModal" @close="isModal = false" @create-task="postTaskFetch"/>
      <!-- <pre>{{ tasks }}</pre> -->
  </div>

  <Footer />
</template>

<script>
import Checkbox from './components/Checkbox.vue';
import Navigation from './components/Navigation.vue';
import Footer from './components/Footer.vue';
import ModalCard from './components/ModalCard.vue';

export default { 
  name: 'Trackly-App',
  components: {
    Navigation,
    Checkbox, 
    ModalCard,
    Footer
  },
  data () {
    return {
      tasks: [],
      isModal: false,
      error: null
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
    },
    async postTaskFetch(newData, path = 'http://127.0.0.1:8000/task') {
      try {
        const response = await fetch(path, {
          method: 'POST', 
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify( newData )
        });

        if (!response.ok) {
          throw new Error(`status: ${response.status}`);
        }
        console.log(newData)

        const createdTask = await response.json();
        this.tasks.push(createdTask)
          
      } catch (error) {
        console.log(newData)
        console.error(error);
      }
    },
    async deleteTaskfetch(path = 'http://127.0.0.1:8000/task') {
      try{
        const response = await 
        fetch(path, {
          method: 'DELETE'
        });

        if (response.ok) {
          console.log('Post deleted successfully.');
        }

      } catch (error){
        console.log(newData)
        console.error(error);
      }
    },
    openModal() {
      console.log(`Modal status: ${this.isModal}`)
      this.isModal = true;
    }
  },
  mounted() {
    this.getTaskFetch();
  }
}
</script>


<style scoped>
.custom-button {
    display: block;
    margin-left: auto;
    background-color: #ffb6c1;
    width: 40px;
    height: 40px;
    text-align: center;
    font-size: 25px;
    font-weight: bold;
    border: 0;
    border-radius: 10px;
    cursor: pointer;
}

.custom-button:hover {
    background-color: #f895a4;
}
</style>