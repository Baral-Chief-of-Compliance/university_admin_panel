<template>
    <div class="text-center">
        <v-dialog
            v-model="dialog"
            width="auto"
        >
            <template v-slot:activator="{ props }">
                <div class="text-h3 py-6 mx-10 text-left">{{ name_dis }}</div>

               
                <v-container class="d-flex justify-center">
                    <v-col>
                        <v-row class="mx-10">
                            <v-col  v-for="f in forms_of_work" :key="f.num_work" cols="12" md="3"  v-bind="props_hover">
                                <v-hover v-slot="{ isHovering, props }" >
                                    <v-card  class="mx-auto" height="200" width="300" 
                                        v-bind="props"
                                        :color="isHovering ? 'indigo': undefined"
                                    >
                                        <v-card-item class="text-h6">
                                            {{ f.name_control }}
                                        </v-card-item>
                                    </v-card>

                                    <v-card-actions class="mt-3">
                                        <v-spacer></v-spacer>
                                        <v-btn @click="delete_work(f.num_work)" variant="outlined" color="red"
                                        >Удалить</v-btn>
                                    </v-card-actions>
                                </v-hover>
                            </v-col>
                        </v-row>    
                        <v-row class="mx-14 mt-15">
                            <v-btn  block
                                color="indigo"
                                v-bind="props"
                            >
                                Добавить форму контроля
                                </v-btn>
                        </v-row>

                    </v-col>
                </v-container>
            </template>

            <v-card>
                <v-card-title>
                    Форма добавления для формы контроля
                </v-card-title>
                <v-form>
                    <v-text-field
                        v-model="name_control"
                        label="Название"
                        color="indigo"
                        class="mx-5 mb-5"
                    >
                    </v-text-field>

                </v-form>
                <v-card-actions>
                    <v-btn color="red"  @click="dialog = false">Закрыть</v-btn>
                    <v-btn color="green"  @click="add_forms_of_work">Добавить</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>    
    </div>
</template>
<script>
import router from "@/router"
import axios from "axios"


export default{
    data: () => ({
        name_dis: "",
        forms_of_work: "",
        dialog: false,
        name_control: "",
        num_dis: ""
    }),

    mounted(){
        this.get_inf_discipline()
    },

    updated(){
        this.get_inf_discipline()
    },

    methods: {
        get_inf_discipline(){
            axios.get(`http://127.0.0.1:5000/disciplines/${this.$route.params.num_dis}`)
            .then(response => (
                this.name_dis = response.data.name_dis,
                this.num_dis = response.data.num_dis,
                this.forms_of_work = response.data.forms_of_work
                ))
        },

        add_forms_of_work(){
            axios.post('http://127.0.0.1:5000/forms_of_work/all', {
                name_control: this.name_control,
                num_dis: this.num_dis
            })
        
            this.name_control = ""

            this.dialog = false
        },

        delete_work(num_work){
            axios.delete(`http://127.0.0.1:5000/forms_of_work/${num_work}`).then(
                (forms_of_work) => this.get_inf_discipline()
            )
        }

    }
}
</script>