<template>
    <div class="Upload container">
    <h2>Upload</h2>
    <UploadForm /> 
 </div>
</template>
<script>
import UploadForm from "@/components/UploadForm.vue";
    export default {
        data() {
            return {};
 },
 components: { UploadForm }  
};
</script>
<style>

form{
    display:flex;
    height:800px;
    width:1000px;
    margin-right:0px;
    flex-direction: column;
}
.result{
    color:rgb(144,77,83);
    font-size: 14px;
    font-weight:600;
    background-color:rgb(248,215,218);
}

.succ-result{
    display:flex;
    background-color:rgb(212,237,218);
    font-size: 14px;
    font-weight:600;
    height:35px;
    width:100%;
    margin-bottom: 5px;
    border-radius: 4px;
    align-items: center;
}

p{
    margin-left:15px;
    margin-bottom:0;
}

.textarea{
    margin-bottom: 21px;
}

.button{
    margin-top:20px;
}

.sub{
    background-color:rgb(41,135,205);
    padding: 4px 20px;
    border-radius:8px;
    color:white;
    font-weight:600;
    border:none;
    width:fit-content;
}
</style>