<template>

    <div className="taskProps">
        <label className="check-container"> 
            <p> {{ tasks.title }} </p>
            <p v-if="tasks.description != 'str'" className="text-description"> -> {{ tasks.description }}</p>
            <input type="checkbox" checked="checked">   
            <span className="checkmark"></span>
        </label>
    </div>
    
</template>


<script type="application/javascript">
export default {
    name: 'Tasks', 
    props: {
        tasks: {
            type: Object, 
            required: true,
        }
    }
};
</script>


<style scoped>
.check-container {
  display: block;
  position: relative;
  padding-left: 38px;
  margin-bottom: 12px;
  cursor: pointer;
  margin-top: 40px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.task-title {
  margin: 0 0 6px 0;
  font-size: 18px;
  font-weight: 600;
  line-height: 1.35;
  color: #222;
  word-break: break-word;
}

.text-description {
  margin: 0;
  font-size: 14px;
  font-weight: 400;
  line-height: 1.5;
  color: #6c757d;
  word-break: break-word;
}

.check-container input {
  position: absolute;
  opacity: 0;
  cursor: pointer;
  height: 0;
  width: 0;
}

.checkmark {
  position: absolute;
  top: 0;
  left: 0;
  height: 24px;
  width: 24px;
  background-color: #eee;
  border-radius: 6px;
  transition: background-color 0.2s ease;
}

.check-container:hover input ~ .checkmark {
  background-color: #ccc;
}

.check-container input:checked ~ .checkmark {
  background-color: #f895a4;
}

.checkmark:after {
  content: "";
  position: absolute;
  display: none;
}

.check-container input:checked ~ .checkmark:after {
  display: block;
}

.check-container .checkmark:after {
  left: 9px;
  top: 5px;
  width: 5px;
  height: 10px;
  border: solid white;
  border-width: 0 3px 3px 0;
  -webkit-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  transform: rotate(45deg);
}

</style>