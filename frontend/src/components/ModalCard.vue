<template>

    <div v-if="showing">
        <section className="modal hidden">
            <button class="close-button" @click="$emit('close')">⨉</button>

            <div>
                <h3>Add new Task</h3>
                <p>Some text</p>
            </div>
            
            <input type="text" id="title" v-model="title" placeholder="Write the name of Task.." />
            <input type="text" id="desctiption" v-model="description" placeholder="Write the description of Task.." />
            <button class="btn" @click="submitData">Submit</button>
        </section>
    </div>

</template>

<script>
export default {
    name: 'ModalCard', 
    props: {
        showing: {
            type: Boolean, 
            required: true
        }, 
    },
    emits: ['close', 'create-task'],
    data() {
        return {
            title: '', 
            description: ''
        }
    },
    methods: {
        submitData() {
            if (!this.title.trim()) {
                return;
            }
            this.$emit('create-task', {
                title: this.title, 
                description: this.description
            })

            this.title = '';
            this.description = '';
            this.$emit('close');
        }
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

.modal {
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 0.4rem;
  width: 450px;
  padding: 1.3rem;
  min-height: 250px;
  position: absolute;
  top: 20%;
  background-color: white;
  border: 1px solid #ddd;
  border-radius: 15px;
  /* transform: translateX(-50%); */
}

.modal .flex {
  display: flex;
  align-items: center;
  /* justify-content: space-between; */
}

.modal input {
  padding: 0.7rem 1rem;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 0.9em;
}

.modal p {
  font-size: 0.9rem;
  color: #777;
  margin: 0.4rem 0 0.2rem;
}

button {
  cursor: pointer;
  border: none;
  font-weight: 600;
}

.btn {
  display: inline-block;
  padding: 0.8rem 1.4rem;
  font-weight: 700;
  background-color: #f895a4;
  color: white;
  border-radius: 5px;
  text-align: center;
  font-size: 1em;
}
/* 
.btn-open {
  position: absolute;
  bottom: 150px;
} */

.close-button {
  position: absolute;
  top: 15px;
  right: 15px;
  width: 30px;
  height: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #eee;
  border-radius: 50%;
  cursor: pointer;
}

</style>