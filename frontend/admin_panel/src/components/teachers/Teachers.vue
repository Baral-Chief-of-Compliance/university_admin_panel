<template>
    <div class="text-center">
        <v-dialog
            v-model="dialog"
            width="auto"
        >
            <template v-slot:activator="{ props }">
                <div class="text-h3 py-6 mx-10 text-left">Преподаватели</div>

               
                <div class="py-6 mx-10 d-flex justify-center" >
                    <v-col>
                        <div v-for="t in teachers">
                            <v-hover v-slot="{ isHovering, props }" >
                                <v-card  class="my-2 pa-6 mx-14 d-flex flex-row"
                                    v-bind="props"
                                    :color="isHovering ? 'indigo': undefined"
                                    :to="{ name: 'teacher', params: {num_t: t.num_t}}"
                                >
                                    <b class="pr-2">Фамилия:</b>  {{ t.surname_t }} 
                                    <v-spacer></v-spacer> 
                                    <b class="pr-2">Имя:</b> 
                                    {{ t.name_t }} 
                                    <v-spacer></v-spacer> 
                                    <b class="pr-2">Отчество:</b>  
                                    {{ t.patri_t }} 
                                    <v-spacer></v-spacer> 
                                    <b class="pr-2">Должность:</b>
                                    {{ t.post  }}
                                </v-card>
                            </v-hover>
                        </div>
                        <div class="my-2 pt-6 mx-14 d-flex flex-row">
                            <v-btn  block
                                color="indigo"
                                v-bind="props"
                            >
                                Добавить преподавателя
                                </v-btn>
                        </div>

                    </v-col>
                </div>
            </template>

            <v-card>
                <v-card-title>
                    Форма для добавления преподавателя
                </v-card-title>
                <v-form>
                    <v-text-field
                        v-model="surname_t"
                        label="Фамилия"
                        color="indigo"
                        class="mx-5 mb-1"
                    >
                    </v-text-field>

                    <v-text-field
                        v-model="name_t"
                        label="Имя"
                        color="indigo"
                        class="mx-5 mb-1"
                    >
                    </v-text-field>

                    <v-text-field
                        v-model="patri_t"
                        label="Отчество"
                        color="indigo"
                        class="mx-5 mb-1"
                    >
                    </v-text-field>

                    <v-text-field
                        v-model="post"
                        label="Должность"
                        color="indigo"
                        class="mx-5 mb-1"
                    >
                    </v-text-field>

                </v-form>
                <v-card-actions>
                    <v-btn color="red"  @click="dialog = false">Закрыть</v-btn>
                    <v-btn color="green"  @click="add_teacher">Добавить</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>    
    </div>
</template>
<script>
import axios from "axios"


export default{
    data: () => ({
        teachers: [],
        dialog: false,
        surname_t: "",
        name_t: "",
        patri_t: "",
        post: ""
    }),

    mounted(){
        this.get_teachers()
    },

    updated(){
        this.get_teachers()
    },

    methods: {
        get_teachers(){
            axios.get('http://127.0.0.1:5000/teachers/all')
            .then(response => (this.teachers = response.data))
        },

        add_student(){
            axios.post('http://127.0.0.1:5000/teachers/all', {
                surname_t: this.surname_t,
                name_t: this.name_t,
                patri_t: this.patri_t,
                post: this.post,
            })
            
            this.surname_t = ""
            this.name_t = ""
            this.patri_t = ""
            this.post = ""

            this.dialog = false
        }
    }
}
</script>