<template>
    <div class="text-center">
        <v-dialog
            v-model="dialog"
            width="auto"
        >
            <template v-slot:activator="{ props }">
                <div class="text-h3 py-6 mx-10 text-left">Дисциплины</div>

               
                <v-container class="d-flex justify-center">
                    <v-col>
                        <v-row class="mx-10">
                            <v-col  v-for="d in disciplines" :key="d.num_dis" cols="12" md="3"  v-bind="props_hover">
                                <v-hover v-slot="{ isHovering, props }" >
                                    <v-card  class="mx-auto" height="200" width="300" 
                                        v-bind="props"
                                        :color="isHovering ? 'indigo': undefined"
                                        :to="{ name: 'discipline', params: {num_dis: d.num_dis}}"
                                    >
                                        <v-card-item class="text-h6">
                                            {{ d.name_dis }}
                                        </v-card-item>
                                    </v-card>

                                    <v-card-actions class="mt-3">
                                        <v-spacer></v-spacer>
                                        <v-btn @click="delete_discipline(d.num_dis)" variant="outlined" color="red"
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
                                Добавить дисциплину
                                </v-btn>
                        </v-row>

                    </v-col>
                </v-container>
            </template>

            <v-card>
                <v-card-title>
                    Форма для добавления дисциплины
                </v-card-title>
                <v-form>
                    <v-text-field
                        v-model="name_dis"
                        label="Название"
                        color="indigo"
                        class="mx-5 mb-5"
                    >
                    </v-text-field>

                </v-form>
                <v-card-actions>
                    <v-btn color="red"  @click="dialog = false">Закрыть</v-btn>
                    <v-btn color="green"  @click="add_discipline">Добавить</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>    
    </div>
</template>
<script>
import axios from "axios"


export default{
    data: () => ({
        disciplines: [],
        dialog: false,
        name_dis: ""
    }),

    mounted(){
        this.get_disciplines()
    },

    updated(){
        this.get_disciplines()
    },

    methods: {
        get_disciplines(){
            axios.get('http://127.0.0.1:5000/disciplines/all')
            .then(response => (this.disciplines = response.data))
        },

        add_discipline(){
            axios.post('http://127.0.0.1:5000/disciplines/all', {
                name_dis: this.name_dis,
            })
            
            this.name_dis = ""

            this.dialog = false
        },

        delete_discipline(num_dis){
            axios.delete(`http://127.0.0.1:5000/disciplines/${num_dis}`).then(
                (disciplines) => this.get_disciplines()
            )
        }

    }
}
</script>