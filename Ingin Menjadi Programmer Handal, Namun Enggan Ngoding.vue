<template>
    <div>
        <h1>{{ pageTitle }}</h1>
    </div>

    <p> 
        Sebagai seorang programmer, tentu kita harus bisa menguasai bahasa pemrograman. 
        Namun, tidak sedikit orang yang ingin menjadi programmer handal, namun enggan untuk belajar ngoding. 
        Padahal, belajar ngoding itu mudah kok. 
        Yang penting adalah konsisten dan tekun dalam belajar. 
        Jangan pernah menyerah, karena semua orang pasti bisa belajar ngoding. 
        Jadi, jangan malas belajar ngoding ya!
    </p>

    <button>
        <router-link to="/">Kembali</router-link>
    </button>
</template>

<script>
export default {
    data() {
        return {
            pageTitle: "Ingin Menjadi Programmer Handal, Namun Enggan Ngoding"
        };
    }
};
</script>

<style>
</style>