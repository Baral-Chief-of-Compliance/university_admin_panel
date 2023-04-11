<template>
    <v-list-group value="Students">
    <template v-slot:activator="{ props }">
      <v-list-item
        v-bind="props"
        prepend-icon="mdi-account-multiple"
        title="Студенты"
      ></v-list-item>
    </template>

    <v-list-item
      v-for="([title, icon, to], i) in students"
      :key="i"
      :title="title"
      :prepend-icon="icon"
      :value="title"
      :to="to"
    ></v-list-item>
  </v-list-group>

  <v-list-group value="Teachers">
    <template v-slot:activator="{ props }">
      <v-list-item
        v-bind="props"
        prepend-icon="mdi-account-details"
        title="Преподаватели"
      ></v-list-item>
    </template>

    <v-list-item
      v-for="([title, icon, to], i) in teachers"
      :key="i"
      :title="title"
      :prepend-icon="icon"
      :value="title"
      :to="to"
    ></v-list-item>

    
  </v-list-group>

  <v-list-group value="Stocks">
    <template v-slot:activator="{ props }">
      <v-list-item
        v-bind="props"
        prepend-icon="mdi-garage"
        title="Склады"
      ></v-list-item>
    </template>

    <v-list-item
      v-for="([title, icon, to], i) in stocks"
      :key="i"
      :title="title"
      :prepend-icon="icon"
      :value="title"
      :to="to"
    ></v-list-item>

    
  </v-list-group>

  <v-list-group value="Orders">
    <template v-slot:activator="{ props }">
      <v-list-item
        v-bind="props"
        prepend-icon="mdi-application"
        title="Заказы"
      ></v-list-item>
    </template>

    <v-list-item
      v-for="([title, icon, to], i) in orders"
      :key="i"
      :title="title"
      :prepend-icon="icon"
      :value="title"
      :to="to"
    ></v-list-item>

    
  </v-list-group>
</template>

<script>
  export default {
    data: () => ({
        students: [
        ['Список', 'mdi-account-multiple', '/students'],
      ],
      teachers:[
        ['Список', 'mdi-account-multiple', '/teachers'],
      ],
      stocks:[
        ['Список', 'mdi-garage', '/stocks'],
        ['Карта', 'mdi-map', '/map_stocks']
      ],
      orders: [
        ['Добавить', 'mdi-plus-outline', '/add_application'],
        ['Активные', 'mdi-file-outline', '/all_active_application'],
        ['Закрытые', 'mdi-update', '/all_close_application']
      ],
    }),
  }
</script>