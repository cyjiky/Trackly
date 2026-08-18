<script>
export default {
    data() {
        return {
            postData: {
                title: '', 
                description: ''
            }
        }
    }
}
</script>

<template>
    <div className="custom-button" @click="postTask">+</div>
</template>

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
    border-radius: 10px;
    cursor: pointer;
}

.custom-button:hover {
    background-color: #f895a4;
}
</style>