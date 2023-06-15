<script setup>
import { Head } from '@inertiajs/vue3'

defineProps({ foo: String })
</script>

<template>
    <Head title="Test" />
    <p>foo? {{ foo }}!</p>
</template>
