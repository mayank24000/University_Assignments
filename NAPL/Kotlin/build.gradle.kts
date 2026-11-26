plugins {
    kotlin("jvm") version "1.9.0"
}

repositories {
    mavenCentral()
}

dependencies {
    implementation(kotlin("stdlib"))
}

sourceSets {
    main {
        kotlin.srcDir(".")
        kotlin.exclude("build/**")
    }
}

tasks.register<JavaExec>("runKotlin") {
    group = "application"
    description = "Runs the Kotlin example."
    dependsOn(tasks.named("classes"))
    classpath = sourceSets.main.get().runtimeClasspath
    mainClass.set("kotlincourse.MainKt")
}
