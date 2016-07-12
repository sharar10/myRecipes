//
//  ViewController.swift
//
//  Copyright 2011-present Parse Inc. All rights reserved.
//

import UIKit
import Parse

class ViewController: UIViewController {
    var names = [""]
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        var query = PFQuery(className:"myRecipes")
        query.findObjectsInBackgroundWithBlock {
            
            (objects: [AnyObject]?, error: NSError?) -> Void in
            
            if error == nil {

                    println(objects)
                // Do something with the found objects

                
            } else {
                // Log details of the failure
                println("Error: \(error!) \(error!.userInfo!)")
            }
        }
        
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
}

