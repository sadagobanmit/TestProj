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
			
			stage ("Clone MSH source") {

                dir('TestProj') {
                    git(
                        branch: 'develop',
                        changelog: false,
                        credentialsId: '829049af-793b-48cf-9e35-5978930370db',
                        poll: false,
						url: 'https://github.com/sadagobanmit/TestProj.git'                        
                    )
                }
            } 
			

            stage ("Build") {
                withEnv(
                    [                     
                        "JOB_NAME=10.1 Test Project"
                    ]
                ) {
                    dir('TestProj\\PythonTest\\Test') {
					
						bat 'python -m unittest helloworldtest'						
                    }
                }
            }       
            
        } catch (e) {
            currentBuild.result = "FAILED"
            throw e
        }
    }
}


