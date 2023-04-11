<template>

    <div class="text-h3 py-6 mx-10 text-left">{{ name_t }} {{ patri_t }} {{ surname_t }}</div>

    <div class="py-6 mx-10 d-flex justify-center" >
        <v-col>
            <v-card  class="my-2 pa-6 mx-14 d-flex flex-row">
                <b class="pr-2">Должность:</b>  {{ post }} 
            </v-card>
        </v-col>
    </div>

    <div class="text-h5 py-6 mx-10 text-left">Нагрузка</div>

    <div v-for="w in workload" class="mx-15 d-flex justify-center" >
        <v-col>
            <v-card  class="pa-6 d-flex flex-row">
                <b class="pr-2">Дисциплина:</b>  {{ w.name_dis }} 
                <v-spacer></v-spacer> 
                <b class="pr-2">Название контроля:</b>  {{ w.name_control }} 
                <v-spacer></v-spacer>
                <b class="pr-2">Курс:</b>  {{ w.course }}
                <v-spacer></v-spacer>
                <b class="pr-2">Семестр:</b>  {{ w.semester }}
                <v-spacer></v-spacer>
                <b class="pr-2">Часы:</b>  {{ w.hours }}
                <v-spacer></v-spacer>
            </v-card>
            <v-card-actions class="mt-3">
                <v-spacer></v-spacer>
                <v-btn @click="delete_delivery(d.num_credit)" variant="outlined" color="red"
                >Удалить</v-btn>
            </v-card-actions>
        </v-col>
    </div>

    <v-row class="mx-14 mt-15">
        <v-btn  block
            color="indigo"
            v-bind="props"
            :to="{ name: 'add_workload', params: {num_t:  this.$route.params.num_t }}"
        >
            Добавить нагрузку
        </v-btn>
    </v-row>
</template>

<script>
import axios from 'axios';

export default{
    data: () => ({
        name_t: "",
        patri_t: "",
        surname_t: "",
        post: "",

        workload: []

    }),
    mounted(){
        this.get_data()
    },

    methods: {
        get_data(){
            axios.get(`http://127.0.0.1:5000/teachers/${this.$route.params.num_t}`)
            .then(response => (
                this.name_t = response.data.name_t,
                this.patri_t = response.data.patri_t,
                this.surname_t = response.data.surname_t,
                this.post = response.data.post,
                this.workload = response.data.workload
            ))
        }
    }
}
</script>