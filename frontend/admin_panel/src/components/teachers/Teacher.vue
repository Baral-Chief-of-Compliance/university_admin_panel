<template>
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
export default{
    data(){
        
    }
}
</script>