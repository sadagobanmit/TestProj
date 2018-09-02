node('master') {
    // We have to checkout to a workspace with a shorted path to get around windows path name restrictions.
    // This also has a side benefit of ensuring that the worker will only use the amount of disk space
    // needed for a single build. The downside is that we can never run concurrent builds on this worker
    // and the workspaces are lost after the next build runs
    ws("C:\\wsws") {

        try {
            stage ("Clean Workspace") {
                deleteDir()
            }

            stage ("Build") {
                withEnv(
                    [
                        "PATH=${env.PATH};C:\\Program Files\\Git\\usr\\bin",                        
                        "JOB_NAME=10.1 Test Project"
                    ]
                ) {
                    dir('E:\\WSNTSrc\\Releases\\TestProj\\TestProj\\HelloWorld') {
					
						mkdir build
						cd build
						cmake -G"Visual Studio 12 2013 Win64" ..
						cmake --build .
                        // sh.exe "cmake ../ && cmake --build ."
                    }
                }
            }

            
            
        } catch (e) {
            currentBuild.result = "FAILED"
            throw e
        }
    }
}


