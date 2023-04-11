<template>
    <div class="text-h3 py-6 mx-10 text-left">Добавить сдачу для {{ name_s }} {{ patro_s }} {{ surname_s }}</div>

    <v-row class="d-flex justify-center my-5">
        <v-card v-show="add_workload" class="pa-6" color="green-accent-1">
            Сдача добавлена
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
                        <v-text-field v-model="name_w" type="text" label="Тема" color="indigo"></v-text-field>
                        <v-text-field v-model="date_work" type="date" label="Дата здачи" color="indigo"></v-text-field>
                        <v-text-field v-model="score" type="number" label="Оценка" color="indigo"></v-text-field>
                    </v-row>
                    <v-row class="mt-10">
                        <v-btn block color="indigo" @click="create_delivery()">
                            Добавить сдачу
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
        name_s: "",
        patro_s: "",
        surname_s: "",
        add_workload: false,
        disciplines: [],
        forms_of_work: [],

        stage: 0,

        num_dis: "",
        num_work: "",
        num_credit: "",
        name_w: "",
        date_work: "",
        score: "",
    }),

    methods: {
        get_student(){
            axios.get(`http://127.0.0.1:5000/students/${this.$route.params.num_credit}`)
            .then(response => (
                this.name_s = response.data.name_s,
                this.patro_s = response.data.patro_s,
                this.surname_s = response.data.surname_s,
                this.num_credit = response.data.num_credit
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

        create_delivery(){
            axios.post('http://127.0.0.1:5000/delivery_of_work/all', {
                num_credit: this.num_credit,
                num_work: this.num_work,
                score: this.score,
                date_work: this.date_work,
                name_w: this.name_w
            })

            this.add_workload = true,
            this.stage = 0,
            this.score = "",
            this.date_work = "",
            this.name_w = "",
            this.num_dis = "",
            this.num_work = ""
        },

        enter_stage(){
            if (this.stage === 0){
                this.get_froms_of_work(this.num_dis)
            }
            else if (this.stage === 0){
                this.add_workload = false
            }
            this.stage++
        },

        exit_stage(){
            this.stage--
        },
    },
    mounted(){
        this.get_student()
        this.get_disciplines()
    }
}
</script>