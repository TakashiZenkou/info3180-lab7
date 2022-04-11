<template>
<form @submit.prevent="uploadPhoto" id="uploadForm" enctype="multipart/form-data"> 
    <div>
        <div v-if="a" v-for="champ in champs" class="succ-result">
            <p>{{champ.message}}</p>
        </div>
        <ul class="result" v-if="a === false">
            <li v-for="champ in champs" class="result">{{champ}}</li>
        </ul>
    </div>
    <label for="description">Description:</label>
    <textarea name="description" class="textarea"></textarea>
    <label for="photo">Photo Upload</label>
    <input type="file" id="myFile" name="photo">
    <div class="button">
        <button type="submit" form="uploadForm" value="Submit" class="sub">Submit</button>
    </div>
</form>
</template>

<script>
export default ({
    data() {
        return{
            csrf_token: '',
            champs: [],
            a: '',
        }     
    },
    methods: {
        uploadPhoto(){
            let self = this;
            let uploadForm = document.getElementById('uploadForm');
            let form_data = new FormData(uploadForm);
            fetch('/api/upload',{
                method: "POST",
                body: form_data,
                headers: {
                    'X-CSRFToken': this.csrf_token
                }
            })
            .then(function(response){
                return response.json();
            })
            .then(function(data){
                // display a success message
                console.log(data);;
                if (data.hasOwnProperty("info")){
                    self.champs = data.info;
                    self.a = true;
                }
                else{
                    self.champs = data.errors;
                    self.a = false;
                }
            })
            .catch(function(error){
                console.log(error);
            });
        },
         getCsrfToken() {
            let self = this;
            fetch('/api/csrf-token')
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
                self.csrf_token = data.csrf_token;
             })
        }
    },
    created() {
        this.getCsrfToken();
    },
})
</script>
