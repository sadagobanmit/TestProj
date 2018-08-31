node('localhost') {
    // We have to checkout to a workspace with a shorted path to get around windows path name restrictions.
    // This also has a side benefit of ensuring that the worker will only use the amount of disk space
    // needed for a single build. The downside is that we can never run concurrent builds on this worker
    // and the workspaces are lost after the next build runs
    ws("C:\\wsws") {

        try {
            stage ("Clean Workspace") {
                deleteDir()
            }
            
            } 

            stage ("Build") {
                withEnv(
                    [
                        "PATH=${env.PATH};C:\\Program Files\\Git\\usr\\bin",
                        "ARTIFACT_PATH=C:\\Artifacts",
                        "JOB_NAME=10.1 Test Project"
                    ]
                ) {
                    dir('work-server/iserver/app/buildInstaller') {
                        build_cmd = "" +
                            """ant resolve setResourceProperties CIBuild """ +
                            """-Dvs.path64.2017="C:\\Program Files (x86)\\Microsoft Visual Studio 12.0\\Common7\\IDE\\\\" """ 
                        echo "build_cmd=${build_cmd}"
                        bat build_cmd
                    }
                }
            }

            
            
        } catch (e) {
            currentBuild.result = "FAILED"
            throw e
        }
    }
}

