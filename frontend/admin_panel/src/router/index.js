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
      },
      {
        path: 'disciplines',
        name: 'disciplines',
        component: () => import('@/components/disciplines/Disciplines.vue')
      },
      {
        path: 'discipline/:num_dis',
        name: 'discipline',
        component: () => import('@/components/disciplines/Discipline.vue')
      },
      {
        path: 'add_workload/:num_t',
        name: 'add_workload',
        component: () => import('@/components/workload/AddWorkload.vue')
      }
    ],
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
