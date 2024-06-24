import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
    },
    {
      path: '/home',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    },
    // Yeni router bağlantıları
    {
      path: '/list-lan-devices',
      name: 'listLanDevices',
      component: () => import('../views/ListLanDevices.vue'),
      meta: { requiresAuth: true } // Add meta field for authenticated routes
      
    },
    {
      path: '/port-scanner',
      name: 'portScanner',
      component: () => import('../views/PortScanner.vue'),
      meta: { requiresAuth: true } // Add meta field for authenticated routes

    },
    {
      path: '/task-list',
      name: 'taskList',
      component: () => import('../views/TaskList.vue'),
      meta: { requiresAuth: true } // Add meta field for authenticated routes
    },
    {
      path: '/sniffer',
      name: 'sniffer',
      component: () => import('../views/Sniffer.vue'),
      meta: { requiresAuth: true } // Add meta field for authenticated routes
    },
    {
      path: '/ddos-attack',
      name: 'ddosAttack',
      component: () => import('../views/DDOSAttack.vue'),
      meta: { requiresAuth: true } // Add meta field for authenticated routes
    },
    {
      path: '/encrypt-decrypt-file',
      name: 'encryptDecryptFile',
      component: () => import('../views/EncryptDecryptFile.vue'),
      meta: { requiresAuth: true } // Add meta field for authenticated routes
    },
    {
      path: '/profile',
      name: 'profile',
      component: () => import('../views/Profile.vue'),
      meta: { requiresAuth: true } // Add meta field for authenticated routes
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/Login.vue')
    }
  ]
})

router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem('auth') === 'true';

  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!isAuthenticated) {
      next('/login'); // Giriş yapılmamışsa login sayfasına yönlendir
    } else {
      next(); // Giriş yapılmışsa devam et
    }
  } else {
    next(); // `requiresAuth` meta verisi yoksa her zaman devam et
  }
});


export default router
