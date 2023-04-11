// Composables
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    component: () => import('@/layouts/default/Default.vue'),
    children: [
      {
        path: '',
        name: 'Home',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "home" */ '@/views/Home.vue'),
      },
      {
        path: 'students',
        name: 'students',
        component: () => import('@/components/students/Students.vue')
      },
      {
        path: 'students/:num_credit',
        name: 'student',
        component: () => import('@/components/students/Student.vue')
      },
      {
        path: 'teachers',
        name: 'teachers',
        component: () => import('@/components/teachers/Teachers.vue')
      },
      {
        path: 'teachers/:num_t',
        name: 'teacher',
        component: () => import('@/components/teachers/Teacher.vue')
      }
    ],
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
