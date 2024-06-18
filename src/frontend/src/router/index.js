import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      redirect: '/login'
    },
    {
      path: '/home',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    // Yeni router bağlantıları
    {
      path: '/list-lan-devices',
      name: 'listLanDevices',
      component: () => import('../views/ListLanDevices.vue')
    },
    {
      path: '/port-scanner',
      name: 'portScanner',
      component: () => import('../views/PortScanner.vue')
    },
    {
      path: '/packet-tracker',
      name: 'packetTracker',
      component: () => import('../views/PacketTracker.vue')
    },
    {
      path: '/task-list',
      name: 'taskList',
      component: () => import('../views/TaskList.vue')
    },
    {
      path: '/sniffer',
      name: 'sniffer',
      component: () => import('../views/Sniffer.vue')
    },
    {
      path: '/ddos-attack',
      name: 'ddosAttack',
      component: () => import('../views/DDOSAttack.vue')
    },
    {
      path: '/encrypt-decrypt-file',
      name: 'encryptDecryptFile',
      component: () => import('../views/EncryptDecryptFile.vue')
    },
    {
      path: '/profile',
      name: 'profile',
      component: () => import('../views/Profile.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/Login.vue')
    }
  ]
})

export default router
