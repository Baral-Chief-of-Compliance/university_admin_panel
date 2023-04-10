<template v-slot:activator="{ props }">
     <div class="text-h3 py-6 mx-10 text-left">Студенты</div>

     <div class="py-6 mx-10 d-flex justify-center" >
        <v-col>
            <div v-for="s in students">
                <v-hover v-slot="{ isHovering, props }" >
                    <v-card  class="my-2 pa-6 mx-14 d-flex flex-row"
                        v-bind="props"
                        :color="isHovering ? 'indigo': undefined"
                        :to="{ name: 'student', params: {num_credit: s.num_credit}}"
                    >
                        <b class="pr-2">Фамилия:</b>  {{ s.surname_s }} 
                        <v-spacer></v-spacer> 
                        <b class="pr-2">Имя:</b> 
                        {{ s.name_s }} 
                        <v-spacer></v-spacer> 
                        <b class="pr-2">Отчество:</b>  
                        {{ s.patro_s }} 
                        <v-spacer></v-spacer> 
                        <b class="pr-2">Группа:</b>
                        {{ s.num_group  }}
                        <v-spacer></v-spacer>
                        <b class="pr-2">Номер зачетки:</b>
                        {{ s.num_credit  }}

                    </v-card>
                </v-hover>
            </div>
        </v-col>
     </div>
</template>

<script>
import axios from "axios"


export default{
    data: () => ({
        students: []
    }),

    mounted(){
        this.get_studnets()
    },

    methods: {
        get_studnets(){
            axios.get('http://127.0.0.1:5000/students')
            .then(response => (this.students = response.data))
        }
    }
}
</script>