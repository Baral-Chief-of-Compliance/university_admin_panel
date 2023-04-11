<template>
    <div class="text-h3 py-6 mx-10 text-left">Добавить нагрузку для {{ name_t }} {{ patri_t }} {{ surname_t }}</div>

    <v-row class="d-flex justify-center my-5">
        <v-card v-show="add_workload" class="pa-6" color="green-accent-1">
            Нагрузка добавлена
        </v-card>
    </v-row>

    <div class="py-6 mx-10 d-flex justify-center">
        <v-col>
            <v-row class="ma-10" v-if="stage === 0">
                <v-radio-group v-model="num_dis">
                    <v-radio color="indigo"  v-for="d in disciplines"
                        :value="d.num_dis"
                        :label="`${d.name_dis}`"
                    >
                    </v-radio>                                 
                </v-radio-group>
            </v-row>

            <v-row class="ma-10" v-else-if="stage === 1">
                <v-radio-group v-model="num_work">
                    <v-radio color="indigo"  v-for="f in forms_of_work"
                        :value="f.num_work"
                        :label="`${f.name_control}`"
                    >
                    </v-radio>  
                </v-radio-group>
            </v-row>

            <v-row class="ma-10" v-else-if="stage === 2">
                <v-col>
                    <v-row>
                        <v-text-field v-model="course" type="number" label="Курс" color="indigo"></v-text-field>
                        <v-text-field v-model="hours" type="number" label="Часы" color="indigo"></v-text-field>
                        <v-text-field v-model="semester" type="number" label="Семестр" color="indigo"></v-text-field>
                        <v-text-field v-model="type_of_classes" type="text" label="Вид занятий" color="indigo"></v-text-field>
                    </v-row>
                    <v-row class="mt-10">
                        <v-btn block color="indigo" @click="create_workload()">
                            Добавить нагрузку
                        </v-btn>
                    </v-row>
                </v-col>


            </v-row>


            <v-row class="ma-10">
                <v-btn @click="exit_stage" color="gray" v-if="stage != 0 ">
                    Назад
                </v-btn>

                <v-spacer></v-spacer>
                <v-btn @click="enter_stage" color="indigo" v-if="stage !=2">
                    Вперед
                </v-btn>
            </v-row>
        </v-col>
    </div>
</template>

<script>
import axios from 'axios';


export default{
    data: () => ({
        name_t: "",
        patri_t: "",
        surname_t: "",
        add_workload: false,
        disciplines: [],
        forms_of_work: [],

        stage: 0,

        num_dis: "",
        num_work: "",
        num_t: "",
        course: "",
        hours: "",
        semester: "",
        type_of_classes: ""
    }),

    methods: {
        get_teacher(){
            axios.get(`http://127.0.0.1:5000/teachers/${this.$route.params.num_t}`)
            .then(response => (
                this.name_t = response.data.name_t,
                this.patri_t = response.data.patri_t,
                this.surname_t = response.data.surname_t,
                this.num_t = response.data.num_t
            ))
        },

        get_disciplines(){
            axios.get("http://127.0.0.1:5000/disciplines/all")
            .then(
                response => (
                    this.disciplines = response.data
                )
            )
        },

        get_froms_of_work(num_dis){
            axios.get(`http://127.0.0.1:5000/disciplines/${num_dis}`)
            .then(
                response => (
                    this.forms_of_work = response.data.forms_of_work
                )
            )
        },

        create_workload(){
            axios.post('http://127.0.0.1:5000/workload/all', {
                num_t: this.num_t,
                num_work: this.num_work,
                course: this.course,
                semester: this.semester,
                type_of_classes: this.type_of_classes,
                hours: this.hours
            })

            this.add_workload = true,
            this.stage = 0,
            this.course = "",
            this.hours = "",
            this.semester = "",
            this.type_of_classes = "",
            this.num_dis = "",
            this.num_work = ""
        },

        enter_stage(){
            if (this.stage === 0){
                this.get_froms_of_work(this.num_dis)
            }
            else if (this.stage === 1){
                this.add_inf = false
            }
            this.stage++
        },

        exit_stage(){
            this.stage--
        },
    },
    mounted(){
        this.get_teacher()
        this.get_disciplines()
    }
}
</script>