<template>
    <div class="text-h3 py-6 mx-10 text-left">{{ surname_s }} {{ name_s }} {{ patro_s }}</div>
    <div class="py-6 mx-10 d-flex justify-center" >
        <v-col>
            <v-card  class="my-2 pa-6 mx-14 d-flex flex-row">
                <b class="pr-2">Группа:</b>  {{ num_group }} 
                <v-spacer></v-spacer> 
                <b class="pr-2">Год поступления:</b>  {{ year_of_admission }} 
                <v-spacer></v-spacer>
                <b class="pr-2">Номер зачетки:</b>  {{ num_credit }} 
            </v-card>
        </v-col>
    </div>

    <v-container class="d-flex justify-center">

    </v-container>
</template>

<script>
import axios from 'axios';


export default{
    data(){
        return{
            name_s: null,
            num_credit: null,
            num_group: null,
            patro_s: null,
            surname_s: null,
            year_of_admission: null
        }
    },
    updated(){
        this.get_data()
    },
    mounted(){
        this.get_data() 
    },
    methods: {
        get_data(){
            axios.get(`http://127.0.0.1:5000/students/${this.$route.params.num_credit}`)
            .then(response => (
                this.name_s = response.data.name_s,
                this.num_credit = response.data.num_credit,
                this.num_group = response.data.num_group,
                this.patro_s = response.data.patro_s,
                this.surname_s = response.data.surname_s,
                this.year_of_admission = response.data.year_of_admission
            ))
        }
    }
}
</script>