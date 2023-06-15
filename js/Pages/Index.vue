<script setup>
import { Head } from '@inertiajs/vue3'

defineProps({ name: String })
</script>

<template>
    <Head title="Welcome" />
    <h1>Welcome</h1>
    <p>Hello {{ name }}, welcome to your first Inertia app!@@!!</p>
</template>
